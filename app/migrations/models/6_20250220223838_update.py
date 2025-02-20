from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "tasks" ADD "status" VARCHAR(50)NOT NULL;
        ALTER TABLE "tasks" DROP COLUMN "complete";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "tasks" ADD "complete" BOOLNOT NULL DEFAULT False;
        ALTER TABLE "tasks" DROP COLUMN "status";"""
