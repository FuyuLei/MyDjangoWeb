from core.forms import BootstrapModelForm

from .models import Post


class PostModelForm(BootstrapModelForm):
    class Meta:
        model = Post
        fields = '__all__'