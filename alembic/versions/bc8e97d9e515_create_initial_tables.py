"""create initial tables

Revision ID: bc8e97d9e515
Revises: 
Create Date: 2024-02-21 21:06:48.285417

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc8e97d9e515'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'students',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('grade', sa.String)
    )

    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('subject', sa.String)
    )

    op.create_table(
        'classes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'))
    )

    op.create_table(
        'grades',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('grade', sa.Integer),
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'))
    )


def downgrade() -> None:
    op.drop_table('grades')
    op.drop_table('classes')
    op.drop_table('teachers')
    op.drop_table('students')
