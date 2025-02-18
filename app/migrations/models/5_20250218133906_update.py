from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ADD "password" BYTEA NOT NULL;
        CREATE INDEX "idx_tasks_title_077193" ON "tasks" ("title");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX IF EXISTS "idx_tasks_title_077193";
        ALTER TABLE "users" DROP COLUMN "password";"""
