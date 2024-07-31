import time
from typing import Optional, List
from pydantic import BaseModel


class InputModel(BaseModel):
    """
    Input model, output of converter.
    """
    data_id: str
    prompt: str
    content: str


class RawInputModel(BaseModel):
    """
    Dataset model, output of converter.
    """
    dataset_id: str = time.strftime('%Y%m%d_%H%M%S', time.localtime())
    eval_models: List[str] = ['default']
    input_path: str = "test/data/test_local_json.json"
    output_path: str = "test/outputs/"

    # Dataset setting
    data_format: str = "json"
    dataset: str = "hugging_face"
    datasource: str = ""

    # Huggingface specific setting
    huggingface_split: str = ""

    column_id: List[str] = []
    column_prompt: List[str] = []
    column_content: List[str] = []

    custom_config_path: Optional[str] = None
