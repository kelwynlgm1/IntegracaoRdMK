from django.urls import path

from .views import PostAPIView, ClientesApiView, CadastradoApiView, NaoCadastradoApiView, InstaladoApiView, \
    update_cliente, update_cliente_cadastrado, UpdateApiView

app_name = 'clientes'
urlpatterns = [
    path('adiciona/clientes', PostAPIView.as_view(), name='clientes'),
    path('update/clientes', UpdateApiView.as_view(), name='update-_clientes'),
    path('visualiza/cadastrados', CadastradoApiView.as_view(), name='cadastrados'),
    path('deleta/cadastrados/<int:id>/', CadastradoApiView.as_view(), name='delete_cadastrados'),
    path('update/cadastrados/', update_cliente_cadastrado, name='update_cadastrados'),
    path('visualiza/nao_cadastrados', NaoCadastradoApiView.as_view(), name='nao_cadastrados'),
    path('update/nao_cadastrados/', update_cliente, name='update_nao_cadastrados'),
    path('deleta/nao_cadastrados/<int:id>/', NaoCadastradoApiView.as_view(), name='delete_nao_cadastrados'),
    path('visualiza/instalados', InstaladoApiView.as_view(), name='instalados'),
    path('visualiza/clientes', ClientesApiView.as_view(), name='get'),
    path('deleta/clientes/<int:id>/', ClientesApiView.as_view(), name='delete')
]