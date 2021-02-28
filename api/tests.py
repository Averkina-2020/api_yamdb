# from django.test import TestCase
from django.urls import reverse


def test_post_id_edit_redirect_for_not_author(self):
    """редирект со страницы /<username>/<post_id>/edit/для тех,
    у кого нет прав доступа к этой странице
    """
    response = self.authorized_client2.get(reverse('post_edit', kwargs={
        'username': self.user,
        'post_id': self.post.id
    }))
    self.assertRedirects(response, reverse('post', kwargs={
        'username': self.user,
        'post_id': self.post.id
    }),
        status_code=302,
        target_status_code=200
    )
