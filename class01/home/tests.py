from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse

from .models import EtapaTrilha, ProgressoUsuario, Topico, Trilha


def _tiny_png():
    # 1x1 PNG
    return SimpleUploadedFile(
        'test.png',
        (
            b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01'
            b'\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00'
            b'\x00\x0cIDATx\x9cc\xf8\x0f\x00\x00\x01\x01\x00\x05\x18'
            b'\xd8N\x00\x00\x00\x00IEND\xaeB`\x82'
        ),
        content_type='image/png',
    )


class HomeViewsTests(TestCase):
    def test_home_empty_db_does_not_crash(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_filter_nivel_experiencia(self):
        icon = _tiny_png()
        img = _tiny_png()
        Topico.objects.create(
            icon_topico=icon,
            nome_topico='Python Test',
            introducao='Intro',
            imagem=img,
            fonte_topic='https://example.com',
            nivel_experiencia='Iniciante',
            ferramentas='',
        )
        response = self.client.get(reverse('all_topics'), {'nivel_experiencia': 'Iniciante'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python Test')


class ProgressoTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('aluno', password='senha12345')
        self.trilha = Trilha.objects.create(
            nome='Fundamentos',
            slug='fundamentos',
            descricao='Desc',
            nivel_alvo='Iniciante',
            ordem=1,
        )
        self.etapa = EtapaTrilha.objects.create(
            trilha=self.trilha,
            ordem=1,
            titulo='Primeira etapa',
            descricao='...',
        )
        self.client = Client()

    def test_toggle_etapa_requires_login(self):
        response = self.client.post(reverse('toggle_etapa', args=[self.etapa.id]))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_toggle_etapa_marks_progress(self):
        self.client.login(username='aluno', password='senha12345')
        response = self.client.post(reverse('toggle_etapa', args=[self.etapa.id]))
        self.assertEqual(response.status_code, 302)
        progresso = ProgressoUsuario.objects.get(usuario=self.user, etapa=self.etapa)
        self.assertTrue(progresso.concluida)
        self.assertEqual(self.trilha.progresso_percentual(self.user), 100)
