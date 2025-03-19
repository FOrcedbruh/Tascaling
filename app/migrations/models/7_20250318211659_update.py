from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "statistics" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "completed_tasks" INT NOT NULL,
    "total_ideas" INT NOT NULL,
    "total_tasks" INT NOT NULL,
    "activity" INT NOT NULL,
    "user_id_id" BIGINT NOT NULL UNIQUE REFERENCES "users" ("id") ON DELETE CASCADE
);
        ALTER TABLE "tasks" ALTER COLUMN "status" SET DEFAULT 'CREATED';
        ALTER TABLE "tasks" ALTER COLUMN "status" TYPE VARCHAR(11) USING "status"::VARCHAR(11);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "tasks" ALTER COLUMN "status" DROP DEFAULT;
        ALTER TABLE "tasks" ALTER COLUMN "status" TYPE VARCHAR(50) USING "status"::VARCHAR(50);
        DROP TABLE IF EXISTS "statistics";"""
