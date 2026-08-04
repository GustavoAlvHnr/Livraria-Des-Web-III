from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .compra import (
    CompraSerializer, 
    ItensCompraSerializer, 
    CompraUpdateCreateSerializer, 
    ItensCompraCreateUpdateSerializer,
    )
from .editora import EditoraSerializer
from .livro import LivroSerializer, LivroListSerializer, LivroRetrieveSerializer
from .user import UserRegistrationSerializer, UserSerializer