from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from apps.posts.repository import PostRepository
from apps.posts.service import PostService


class PostContainer(DeclarativeContainer):
    config = providers.Configuration()

    post_repository: providers.Dependency[PostRepository] = providers.Singleton(
        PostRepository,
    )

    post_service: providers.Dependency[PostService] = providers.Singleton(
        PostService,
        config=config,
        post_repository=post_repository,
    )