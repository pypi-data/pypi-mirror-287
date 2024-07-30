# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .cost_data import CostData
from .requests_data import RequestsData

__all__ = ["BudgetResponse", "Budget", "BudgetTotals", "BudgetTotalsBudgetTransactions"]


class BudgetTotalsBudgetTransactions(BaseModel):
    blocked: int

    blocked_external: int

    exceeded: int

    successful: int

    error: Optional[int] = None

    total: Optional[int] = None


class BudgetTotals(BaseModel):
    cost: CostData

    requests: RequestsData

    budget_transactions: Optional[BudgetTotalsBudgetTransactions] = None


class Budget(BaseModel):
    base_cost_estimate: Literal["max"]

    budget_creation_timestamp: datetime

    budget_id: str

    budget_name: str

    budget_response_type: Literal["block", "allow"]

    budget_type: Literal["conservative", "liberal"]

    budget_update_timestamp: datetime

    currency: Literal["usd"]

    max: float

    totals: BudgetTotals

    budget_tags: Optional[List[str]] = None


class BudgetResponse(BaseModel):
    budget: Budget

    request_id: str

    message: Optional[str] = None
