"""Run extraction service for a dockerized AI."""
import json
import logging
import os
import typing as t

import bentoml
from fastapi import Depends, FastAPI, HTTPException

from .schemas import ExtractRequest20240117, ExtractResponse20240117
from .utils import prepare_request, process_response

# load ai model name from AI_MODEL_NAME file in parent directory
ai_model_name_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'AI_MODEL_NAME')
ai_model_name = open(ai_model_name_file).read().strip()

app = FastAPI()

logger = logging.getLogger(__name__)


@bentoml.service
@bentoml.mount_asgi_app(app, path='/v1')
class ExtractionService:
    model_ref = bentoml.models.get(ai_model_name)

    def __init__(self):
        """Load the extraction model into memory."""
        self.extraction_model = bentoml.picklable_model.load_model(self.model_ref)

    @bentoml.api(input_spec=ExtractRequest20240117)
    async def extract(self, **request: t.Any) -> ExtractResponse20240117:
        """Send an call to the Extraction AI and process the response."""
        # Even though the request is already validated against the pydantic schema, we need to get it back as an
        # instance of the pydantic model to be able to pass it to the prepare_request function.
        request = ExtractRequest20240117(**request)
        project = self.extraction_model.project
        document = prepare_request(request=request, project=project)
        result = self.extraction_model.extract(document)
        annotations_result = process_response(result)
        return annotations_result


@app.get('/project-metadata')
async def project_metadata(service=Depends(bentoml.get_current_service)):
    """Return the embedded JSON data about the project."""
    project_metadata_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'categories_and_labels_data.json5')
    try:
        with open(project_metadata_file) as f:
            project_metadata = json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail='Project metadata not found')
    return project_metadata
