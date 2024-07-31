from typing import Dict
from typing import List
from typing import Optional

from tecton._internals.tecton_pydantic import StrictModel
from tecton.types import Field


_CUSTOM_MODELS: List["ModelConfig"] = []


class ModelConfig(StrictModel):
    """A Custom Model in Tecton

    ```python
    from tecton import ModelConfig

    model_config = ModelConfig(
        name=”mymodel_text_embedder”,
        model_type="pytorch",
        model_file="model_file.py",
        environments=["custom-ml-env-01"],
        artifact_files=["model.safetensors", "tokenizer_config.json" …],
        input_schema=[Field(”my_text_col”, String), …],
        output_schema=Field(”text_embedding”)
    )
    ```

    :param name: Unique name of model
    :param model_type: Type of Model (pytorch or text embedding)
    :param description: Description of Model
    :param tags: Tags associated with this Tecton Object (key-value pairs of arbitrary metadata).
    :param model_file: Path of File containing model relative to where the Tecton object is defined.
    :param artifact_files: Path of other files needed to load and run model relative to where the Tecton object is defined.
    :param environments: All the environments allowed for this custom model to run in.
    :param input_schema: Input Schema for model.
    :param output_schema: Output Schema of model.

    :raises TectonValidationError: if the input non-parameters are invalid.
    """

    name: str
    model_type: str
    description: Optional[str]
    tags: Optional[Dict[str, str]]
    model_file: str
    artifact_files: Optional[List[str]]
    environments: List[str]
    input_schema: List[Field]
    output_schema: Field

    def __init__(
        self,
        *,
        name: str,
        model_type: str,
        model_file: str,
        environments: List[str],
        input_schema: List[Field],
        output_schema: Field,
        artifact_files: Optional[List[str]] = None,
        description: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
    ):
        super().__init__(
            name=name,
            model_type=model_type,
            model_file=model_file,
            artifact_files=artifact_files,
            environments=environments,
            input_schema=input_schema,
            output_schema=output_schema,
            description=description,
            tags=tags,
        )
        _CUSTOM_MODELS.append(self)
