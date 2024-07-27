from sqlalchemy import Boolean, Column, ForeignKey, Integer
from pixiv_sql.model.base import BaseJoinModel


class IllustTag(BaseJoinModel):
    """
    IllustTag Model
    """

    __tablename__ = "illusts_tags"

    illust_id = Column(Integer, ForeignKey("bookmarked_illusts.id"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tags.id"), primary_key=True)
    is_registered = Column(Boolean, default=False, nullable=False)
