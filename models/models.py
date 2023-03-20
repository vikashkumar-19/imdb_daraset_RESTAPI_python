from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String, TEXT, FLOAT, BOOLEAN, ForeignKeyConstraint, PrimaryKeyConstraint, SMALLINT, ForeignKey

Base = declarative_base()

class Titles(Base):
    __tablename__ = "titles"
    title_id = Column(String(255), nullable=False, primary_key=True)
    title_type = Column(String(50),)
    primary_title = Column(TEXT)
    original_title = Column(TEXT)
    is_adult = Column(BOOLEAN,)
    start_year = Column(INTEGER)
    end_year = Column(INTEGER)
    runtime_minutes = Column(INTEGER)

class Title_ratings(Base):
    __tablename__ = "titles_ratings"
    title_id = Column(String(255), ForeignKey("titles.title_id"), primary_key=True)
    average_rating = Column(FLOAT)
    num_votes = Column(INTEGER)
    # ForeignKeyConstraint(["title_id"],["titles.title_id"])

class Aliases(Base):
    __tablename__ = "aliases"
    title_id = Column(String(255), ForeignKey("titles.title_id"), primary_key=True)
    ordering = Column(INTEGER, primary_key=True)
    title = Column(TEXT, nullable=False)
    region = Column(String(4))
    language = Column(String(4))
    is_original_title = Column(BOOLEAN)
    # PrimaryKeyConstraint(["title_id","ordering"])
    # ForeignKeyConstraint(["title_id"],["titles.title_id"])

class Alias_types(Base):
    __tablename__ = "alias_types"
    title_id = Column(String(255), ForeignKey("titles.title_id"), primary_key=True)
    ordering = Column(INTEGER, primary_key=True)
    type = Column(String(255),nullable=False)
    # PrimaryKeyConstraint("title_id","ordering")
    # ForeignKeyConstraint(["title_id"],["titles.title_id"])

class ALias_attributes(Base):
    __tablename__ = "alias_attributes"
    title_id = Column(String(255), ForeignKey("titles.title_id"), primary_key=True)
    ordering = Column(INTEGER,nullable=False, primary_key=True)
    attribute = Column(String(255),nullable=False)
    # ForeignKeyConstraint(["title_id"],["titles.title_id"])

class Episode_belongs_to(Base):
    __tablename__ = "episode_belongs_to"
    episode_title_id = Column(String(255), ForeignKey("titles.title_id"), primary_key=True)
    parent_tv_show_title_id = Column(String(255), ForeignKey("titles.title_id"))
    season_number = Column(INTEGER)
    episode_number = Column(INTEGER)
    # ForeignKeyConstraint(["episode_title_id","parent_tv_show_title_id"],["titles.title_id", "titles.title_id"])

class Title_genres(Base):
    __tablename__ = "title_genres"
    title_id = Column(String(255), ForeignKey("titles.title_id"), primary_key=True)
    genre = Column(String(255), primary_key=True)
    # PrimaryKeyConstraint("title_id","genre")
    # ForeignKeyConstraint(["title_id"],["titles.title_id"])

class Names_(Base):
    __tablename__ = "names_"
    name_id = Column(String(255),primary_key=True)
    name_ = Column(String(255),nullable=False)
    birth_year = Column(SMALLINT)
    death_year = Column(SMALLINT)


class Name_worked_as(Base):
    __tablename__ = "name_worked_as"
    name_id = Column(String(255),ForeignKey("names_.name_id"), primary_key=True)
    profession = Column(String(255), primary_key=True)
    # PrimaryKeyConstraint("profession","name_id")
    # ForeignKeyConstraint(["name_id"],["names_.name_id"])

class Had_role(Base):
    __tablename__ = "had_role"
    title_id = Column(String(255), ForeignKey("titles.title_id"), primary_key=True)
    name_id = Column(String(255),ForeignKey("names_.name_id"), primary_key=True)
    role_ = Column(TEXT,primary_key=True)
    # PrimaryKeyConstraint("title_id","name_id","role_")
    # ForeignKeyConstraint(["name_id","title_id"],["names_.name_id","titles.title_id"])

class Known_for(Base):
    __tablename__ = "known_for"
    title_id = Column(String(255), ForeignKey("titles.title_id"), primary_key=True)
    name_id = Column(String(255),ForeignKey("names_.name_id"), primary_key=True)
    # PrimaryKeyConstraint("name_id","title_id"),
    # ForeignKeyConstraint(["name_id","title_id"],["names_.name_id","titles.title_id"])

class Directors(Base):
    __tablename__ = "directors"
    title_id = Column(String(255), ForeignKey("titles.title_id"), primary_key=True)
    name_id = Column(String(255),ForeignKey("names_.name_id"), primary_key=True)
    # PrimaryKeyConstraint("title_id","name_id")
    # ForeignKeyConstraint(["name_id","title_id"],["names_.name_id","titles.title_id"])

class Writers(Base):
    __tablename__ = "writers"
    title_id = Column(String(255), ForeignKey("titles.title_id"), primary_key=True)
    name_id = Column(String(255),ForeignKey("names_.name_id"), primary_key=True)
    # PrimaryKeyConstraint("title_id","name_id")
    # ForeignKeyConstraint(["name_id","title_id"],["names_.name_id","titles.title_id"])

class Principals(Base):
    __tablename__ = "principals"
    title_id = Column(String(255), ForeignKey("titles.title_id"), primary_key=True)
    name_id = Column(String(255),ForeignKey("names_.name_id"), primary_key=True)
    ordering = Column(INTEGER,nullable=False)
    job_category = Column(String(255))
    job = Column(TEXT)
    # PrimaryKeyConstraint("title_id","ordering")
    # ForeignKeyConstraint(["name_id","title_id"],["names_.name_id","titles.title_id"])
