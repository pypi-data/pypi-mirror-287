import json
from typing import Any, Dict, Optional, Union, Generator

from dingo.data.dataset.base import Dataset
from dingo.data.utils.digit import compute_pandas_digest
from dingo.data.datasource import DataSource
from dingo.io import InputModel


@Dataset.register()
class SparkDataset(Dataset):
    """
    Represents a HuggingFace dataset for use with Dingo Tracking.
    """

    def __init__(
            self,
            source: DataSource,
            name: Optional[str] = None,
            digest: Optional[str] = None,
    ):
        """
        Args:
            source: The source of the local file data source
            name: The name of the dataset. E.g. "wiki_train". If unspecified, a name is
                automatically generated.
            digest: The digest (hash, fingerprint) of the dataset. If unspecified, a digest
                is automatically computed.
        """
        self._ds = source.load()
        self._targets = "text"
        if source.get_source_type() == "hugging_face" and source.raw_input.data_format == "plaintext":
            if source.raw_input.column_content != '':
                self._targets = source.raw_input.column_content[0]
            if self._targets is not None and self._targets not in self._ds.column_names:
                raise RuntimeError(
                    f"The specified Hugging Face dataset does not contain the specified targets column"
                    f" '{self._targets}'.",
                )
        super().__init__(source=source, name=name, digest=digest)

    @staticmethod
    def get_dataset_type() -> str:
        return "spark"

    def _compute_digest(self) -> str:
        """
        Computes a digest for the dataset. Called if the user doesn't supply
        a digest when constructing the dataset.
        """
        if self.source.get_source_type() == "local":
            return str(hash(json.dumps(self.source.to_dict())))[:8]
        elif self.source.get_source_type() == "hugging_face":
            df = next(self._ds.to_pandas(batch_size=10000, batched=True))
            return compute_pandas_digest(df)
        elif self.source.get_source_type() == "spark":
            pass
        raise RuntimeError("Spark Datasource must in ['local', 'hugging_face', 'spark']")

    def to_dict(self) -> Dict[str, str]:
        """Create config dictionary for the dataset.
        Returns a string dictionary containing the following fields: name, digest, source, source
        type, schema, and profile.
        """
        config = super().to_dict()
        config.update(
            {
                "profile": json.dumps(self.profile),
            }
        )
        return config

    def get_data(self) -> Generator[InputModel, None, None]:
        """
        Returns the input model for the dataset.
        Convert data here.
        """
        # TODO 做成pyspark的dataframe，之后会在spark中使用。
        for data_raw in self._ds:
            if self.source.get_source_type() == "hugging_face" and self._converter == "plaintext":
                data_raw = data_raw[self._targets]
            data: Union[Generator[InputModel], InputModel] = self.converter(data_raw)
            if isinstance(data, Generator):
                for d in data:
                    yield d
            else:
                yield data

    @property
    def ds(self):
        """The Hugging Face ``datasets.Dataset`` instance.
        Returns:
            The Hugging Face ``datasets.Dataset`` instance.
        """
        return self._ds

    @property
    def source(self) -> DataSource:
        """Hugging Face dataset source information.
        Returns:
            A :py:class:`mlflow.data.huggingface_dataset_source.HuggingFaceSource`
        """
        return self._source
