from typing import Any
from pydantic import BaseModel, ConfigDict, field_validator
from pydantic.alias_generators import to_camel
from SolSystem.Models.Common import Base58Str



class Instruction(BaseModel):
    """### Parameters
    `program_id_index:` Index into the message.accountKeys array belonging to the
    parent transaction object indicating the program account that executes this
    instruction.

    `accounts:` List of ordered indices into the message.accountKeys array
    belonging to the parent transaction object indicating which accounts to pass
    to the program.

    `data:` The encoded program input data.

    `stack_height:` UNKNOWN, present in output, but not in documentation."""
    model_config = ConfigDict(
        alias_generator = to_camel,
        populate_by_name = True,
    )

    program_id_index: int
    accounts: list[int]
    data: Base58Str | None = None
    stack_height: Any

    @field_validator("*", mode = "before")
    def prepare_empty_fields(cls, v: Any) -> Any:
        """### Summary
        Instead of NULL the API tends to return empty strings, so we handle that
        by converting to None in the pre validator"""
        if v == "":
            return None
        else:
            return v



class InnerInstruction(BaseModel):
    """### Summary
    The Solana runtime records the cross-program instructions that are invoked
    during transaction processing. Invoked instructions are grouped by the
    originating transaction instruction and are listed in order of processing.
    [Further Details](https://solana.com/docs/rpc/json-structures#inner-instructions)

    ### Parameters
    `index:` Index of the transaction instruction from which the inner
    instruction(s) originated

    `instructions:` Ordered list of inner program instructions that were
    invoked during a single transaction instruction."""
    index: int
    instructions: list[Instruction]