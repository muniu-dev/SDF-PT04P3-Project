"""Your message here

Revision ID: c278c2ffa734
Revises: 
Create Date: 2024-02-21 14:56:46.576534

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c278c2ffa734'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'students',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('grade', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('subject', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    
    op.create_table(
        'classes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('teacher_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    
    op.create_table(
        'grades',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('grade', sa.Integer(), nullable=True),
        sa.Column('student_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('grades')
    op.drop_table('classes')
    op.drop_table('teachers')
    op.drop_table('students')
