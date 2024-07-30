import os

import torch
from torch_geometric.data import Data

from aq_geometric.models.base_model import BaseModel


class TorchBaseModelAdapter(BaseModel, torch.nn.Module):
    """
    Adapter class to provide PyTorch compatibility for BaseModel.
    """

    def __init__(self, *args, **kwargs):
        # Initialize both base classes
        BaseModel.__init__(self, *args, **kwargs)
        torch.nn.Module.__init__(self)

    def forward(self, graph: Data) -> torch.Tensor:
        """
        Forward pass of the PyTorch model.
        (This method is required for torch.nn.Module)

        Args:
            graph (Data): The graph data object from torch_geometric.

        Returns:
            torch.Tensor: The model's output.
        """
        raise NotImplementedError("Forward pass not implemented in the base adapter.")

    def save(self, path: str):
        """Save the model to a file."""
        # ensure the model is on the CPU
        self.cpu()

        # ensure the path exists
        # check if the path has a directory
        if os.path.dirname(path):
            # create the directory if it does not exist
            os.makedirs(os.path.dirname(path), exist_ok=True)

        # gather the model data
        model_data = {
            "name": self.name,
            "guid": self.guid,
            "stations": self.stations,
            "features": self.features,
            "targets": self.targets,
            "num_samples_in_node_feature": self.num_samples_in_node_feature,
            "num_samples_in_node_target": self.num_samples_in_node_target,
            "is_iterative": self.is_iterative,
            "state_dict": self.state_dict(),
            **self.kwargs
        }
        # save the model data
        torch.save(model_data, path)

    def load(self, path: str):
        """Load the model from a file."""
        # load the model data
        model_data = torch.load(path)

        # set the model data
        self.name = model_data["name"]
        self.guid = model_data["guid"]
        self.stations = model_data["stations"]
        self.features = model_data["features"]
        self.targets = model_data["targets"]
        self.num_samples_in_node_feature = model_data["num_samples_in_node_feature"]
        self.num_samples_in_node_target = model_data["num_samples_in_node_target"]
        self.num_features_in_node_feature = len(self.features)
        self.num_features_in_node_target = len(self.targets)
        self.is_iterative = model_data.get("is_iterative", False)  # for backwards compatability
        
        self.load_state_dict(model_data["state_dict"])

        # set the kwargs
        for key, value in model_data.items():
            if key not in ["name", "guid", "stations", "features", "targets", "num_samples_in_node_feature", "num_samples_in_node_target", "num_features_in_node_feature", "num_features_in_node_target", "is_iterative", "state_dict"]:
                setattr(self, key, value)
