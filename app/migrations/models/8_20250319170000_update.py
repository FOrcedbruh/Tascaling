from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "statistics" DROP CONSTRAINT IF EXISTS "fk_statisti_users_7f2f1c48";
        ALTER TABLE "statistics" RENAME COLUMN "user_id_id" TO "user_id";
        ALTER TABLE "statistics" ALTER COLUMN "activity" SET DEFAULT 0;
        ALTER TABLE "statistics" ALTER COLUMN "total_tasks" SET DEFAULT 0;
        ALTER TABLE "statistics" ALTER COLUMN "total_ideas" SET DEFAULT 0;
        ALTER TABLE "statistics" ALTER COLUMN "completed_tasks" SET DEFAULT 0;
        ALTER TABLE "statistics" ADD CONSTRAINT "fk_statisti_users_d5778ec3" FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "statistics" DROP CONSTRAINT IF EXISTS "fk_statisti_users_d5778ec3";
        ALTER TABLE "statistics" RENAME COLUMN "user_id" TO "user_id_id";
        ALTER TABLE "statistics" ALTER COLUMN "activity" DROP DEFAULT;
        ALTER TABLE "statistics" ALTER COLUMN "total_tasks" DROP DEFAULT;
        ALTER TABLE "statistics" ALTER COLUMN "total_ideas" DROP DEFAULT;
        ALTER TABLE "statistics" ALTER COLUMN "completed_tasks" DROP DEFAULT;
        ALTER TABLE "statistics" ADD CONSTRAINT "fk_statisti_users_7f2f1c48" FOREIGN KEY ("user_id_id") REFERENCES "users" ("id") ON DELETE CASCADE;"""
