# coding: utf-8

# Copyright 2023 Inria (Institut National de Recherche en Informatique
# et Automatique)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""q-Federated Learning Aggregator class."""

from typing import Any, Dict, List

from declearn.aggregator._api import Aggregator, ModelUpdates
from declearn.model.api import Vector


__all__ = [
    "QFLAggregator",
]


class QFLAggregator(Aggregator[ModelUpdates]):
    """Aggregator subclass implementing q-Federated Learning.

    This `Aggregator` subclass implements both the q-FedSGD
    and q-FedAvg algorithms introduced in paper [1].

    References
    ----------
    - Li et al. (2019).
      Fair Resource Allocation in Federated Learning.
      https://arxiv.org/abs/1905.10497
    """

    name = "q-fl"

    def __init__(
        self,
        q_val: int,
        l_val: float = 1.0,
    ) -> None:
        """Instantiate the q-FederatedLearning aggregator.

        Parameters
        ----------
        q_val:
            Value of the q parameter, scaling the influence of the model's
            training loss in the assignment of client averaging weights.
        l_val:
            Value of the estimated Lipschitz constant to use when running
            multiple local steps per round. Use `l_val=1.0` (the default)
            when running a single step per round (q-FedSGD). We advise
            using `l_val=1/lrate` when running multiple steps per round
            (q-FedAvg).
        """
        if not isinstance(q_val, int) and q_val >= 0:
            raise TypeError("'q_val' parameter must be a positive int.")
        self.q_val = q_val
        self.l_val = l_val

    def get_config(
        self,
    ) -> Dict[str, Any]:
        return {
            "q_val": self.q_val,
            "l_val": self.l_val,
        }

    def prepare_for_sharing(
        self,
        updates: Vector,
        n_steps: int,
        losses: List[float],
    ) -> ModelUpdates:
        # Scale updates by L (skip if L = 1.0 to avoid useless operations).
        if self.l_val != 1.0:
            updates = updates * self.l_val
        # Fetch the training loss of the initial model weights (on a batch).
        if not losses:
            raise RuntimeError("Cannot apply q-FL aggregation without a loss.")
        loss = losses[0]
        loss_q = pow(loss, self.q_val)
        # Compute the euclidean norm of the (L-scaled) model updates.
        # NOTE: is this the proper || ||^2 norm from the paper?
        # NOTE: this could be refactored as a Vector method (in the future).
        sum_of_squares = (updates**2).sum()
        total_sum_of_squares = sum(
            type(updates)({"norm": value})
            for value in sum_of_squares.coefs.values()
        )
        l2_norm = (total_sum_of_squares**0.5).flatten()[0][0]
        # Compute the numerator and denominator of the updates.
        num = loss_q * updates
        den = self.q_val * pow(loss, self.q_val - 1) * l2_norm
        den += self.l_val * loss_q
        # Wrap as a `ModelUpdates` for (secure-)aggregation and return.
        return ModelUpdates(updates=num, weights=den)

    def finalize_updates(
        self,
        updates: ModelUpdates,
    ) -> Vector:
        return updates.updates / updates.weights
