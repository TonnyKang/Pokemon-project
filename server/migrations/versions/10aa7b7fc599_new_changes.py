"""New changes

Revision ID: 10aa7b7fc599
Revises: 340966e4d7d5
Create Date: 2024-11-27 11:13:50.895688

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '10aa7b7fc599'
down_revision = '340966e4d7d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokedex')
    op.drop_table('pokemon')
    op.drop_table('typeeffectiveness')
    op.drop_table('pokemonmoves')
    op.drop_table('moves')
    op.drop_table('gymbattlerecords')
    op.drop_table('trainers')
    op.drop_table('wildbattlerecords')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wildbattlerecords',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('trainer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('pokemon_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('result', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.id'], name='wildbattlerecords_pokemon_id_fkey'),
    sa.ForeignKeyConstraint(['trainer_id'], ['trainers.id'], name='wildbattlerecords_trainer_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='wildbattlerecords_pkey')
    )
    op.create_table('trainers',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('trainers_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('badges', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=True),
    sa.Column('role', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='trainers_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('gymbattlerecords',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('trainer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('gym_leader_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('result', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['gym_leader_id'], ['trainers.id'], name='gymbattlerecords_gym_leader_id_fkey'),
    sa.ForeignKeyConstraint(['trainer_id'], ['trainers.id'], name='gymbattlerecords_trainer_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='gymbattlerecords_pkey')
    )
    op.create_table('moves',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('moves_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('type', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('power', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pp', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('accuracy', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='moves_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('pokemonmoves',
    sa.Column('pokemon_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('move_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('remaining_uses', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['move_id'], ['moves.id'], name='pokemonmoves_move_id_fkey'),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.id'], name='pokemonmoves_pokemon_id_fkey'),
    sa.PrimaryKeyConstraint('pokemon_id', 'move_id', name='pokemonmoves_pkey')
    )
    op.create_table('typeeffectiveness',
    sa.Column('attack', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('defend', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('effectiveness', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('attack', 'defend', name='typeeffectiveness_pkey')
    )
    op.create_table('pokemon',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('pokemon_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('level', sa.INTEGER(), server_default=sa.text('1'), autoincrement=False, nullable=True),
    sa.Column('experience', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=True),
    sa.Column('hp', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('trainer_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokedex.id'], name='pokemon_pokemon_id_fkey'),
    sa.ForeignKeyConstraint(['trainer_id'], ['trainers.id'], name='pokemon_trainer_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='pokemon_pkey')
    )
    op.create_table('pokedex',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('type1', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('type2', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('hp_stat', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('att', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('def', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('spd', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='pokedex_pkey')
    )
    # ### end Alembic commands ###
