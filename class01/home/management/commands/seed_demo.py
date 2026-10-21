from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand

from home.models import EtapaTrilha, Ferramenta, Topico, Trilha


class Command(BaseCommand):
    help = 'Cria 2 trilhas demo, etapas e ferramentas reais nos tópicos-chave.'

    def handle(self, *args, **options):
        self._seed_ferramentas()
        self._seed_trilhas()
        self.stdout.write(self.style.SUCCESS('Seed demo concluído.'))

    def _find_asset(self, *candidates):
        root = Path(__file__).resolve().parents[4] / 'assets-p.i'
        for name in candidates:
            for path in root.rglob(name):
                if path.is_file():
                    return path
        return None

    def _attach_image(self, instance, field_name, *asset_names):
        field = getattr(instance, field_name)
        if field and field.name:
            media_path = Path(field.path) if hasattr(field, 'path') else None
            if media_path and media_path.exists():
                return
        asset = self._find_asset(*asset_names)
        if not asset:
            return
        with asset.open('rb') as fh:
            getattr(instance, field_name).save(asset.name, File(fh), save=True)

    def _seed_ferramentas(self):
        tools = [
            {
                'topico': 'Python',
                'nome': 'Django',
                'info': 'Framework web em Python para construir aplicações completas com ORM, admin e templates.',
                'link': 'https://www.djangoproject.com/',
                'assets': ('django_img.jfif', 'django_img.jfif'),
            },
            {
                'topico': 'Python',
                'nome': 'PyCharm',
                'info': 'IDE da JetBrains focada em Python, com debugger, refatoração e suporte a Django.',
                'link': 'https://www.jetbrains.com/pycharm/',
                'assets': ('pycharm_img.webp',),
            },
            {
                'topico': 'HTML5',
                'nome': 'MDN Web Docs',
                'info': 'Documentação oficial de referência para HTML, CSS e JavaScript mantida pela Mozilla.',
                'link': 'https://developer.mozilla.org/pt-BR/docs/Web/HTML',
                'assets': ('html5.png',),
            },
            {
                'topico': 'CSS3',
                'nome': 'Tailwind CSS',
                'info': 'Framework de utilitários CSS para montar interfaces modernas sem sair do HTML.',
                'link': 'https://tailwindcss.com/',
                'assets': ('tailwind-css.jpeg',),
            },
            {
                'topico': 'Javascript',
                'nome': 'Node.js',
                'info': 'Runtime JavaScript no servidor, base para backend e ferramentas do ecossistema frontend.',
                'link': 'https://nodejs.org/',
                'assets': ('icon-javascript.png',),
            },
            {
                'topico': 'Gestão de Projetos',
                'nome': 'Trello',
                'info': 'Quadro Kanban visual para organizar tarefas e acompanhar o fluxo do projeto.',
                'link': 'https://trello.com/',
                'assets': ('app_trello.jpg',),
            },
        ]

        for item in tools:
            topico = Topico.objects.filter(nome_topico__iexact=item['topico']).first()
            if not topico:
                self.stdout.write(self.style.WARNING(f'Tópico não encontrado: {item["topico"]}'))
                continue
            ferramenta = Ferramenta.objects.filter(
                topico=topico,
                nome_ferramenta=item['nome'],
            ).first()
            if not ferramenta:
                ferramenta = Ferramenta(
                    topico=topico,
                    nome_ferramenta=item['nome'],
                    informacao_ferramenta=item['info'],
                    link_ferramenta=item['link'],
                )
                asset = self._find_asset(*item['assets'])
                if not asset:
                    self.stdout.write(self.style.WARNING(f'Sem imagem para {item["nome"]}, pulando.'))
                    continue
                with asset.open('rb') as fh:
                    ferramenta.imagem_ferramenta.save(asset.name, File(fh), save=False)
                ferramenta.save()
            else:
                ferramenta.informacao_ferramenta = item['info']
                ferramenta.link_ferramenta = item['link']
                ferramenta.save(update_fields=['informacao_ferramenta', 'link_ferramenta'])
                self._attach_image(ferramenta, 'imagem_ferramenta', *item['assets'])
            self.stdout.write(f'Ferramenta: {ferramenta.nome_ferramenta} ({topico.nome_topico})')

    def _get_topico(self, *names):
        for name in names:
            topico = Topico.objects.filter(nome_topico__iexact=name).first()
            if topico:
                return topico
            topico = Topico.objects.filter(nome_topico__icontains=name).first()
            if topico:
                return topico
        return None

    def _seed_trilhas(self):
        fundamentos, _ = Trilha.objects.update_or_create(
            slug='fundamentos',
            defaults={
                'nome': 'Fundamentos da Programação',
                'descricao': (
                    'Do zero à lógica: entenda o mercado, pense em algoritmos e escolha as primeiras ferramentas.'
                ),
                'nivel_alvo': 'Iniciante',
                'ordem': 1,
                'ativa': True,
            },
        )
        frontend, _ = Trilha.objects.update_or_create(
            slug='frontend',
            defaults={
                'nome': 'Frontend Web',
                'descricao': (
                    'Construa interfaces: HTML, CSS, JavaScript e o papel do frontend no produto digital.'
                ),
                'nivel_alvo': 'Iniciante',
                'ordem': 2,
                'ativa': True,
            },
        )

        fund_steps = [
            (1, 'Como começar na programação', 'Visão geral das áreas e do primeiro passo.',
             ('Lógica de Programação',), 'https://www.freecodecamp.org/portuguese/news/'),
            (2, 'Lógica de programação', 'Variáveis, condicionais e laços — a base de tudo.',
             ('Lógica de Programação',), ''),
            (3, 'Algoritmos', 'Como descrever soluções passo a passo.',
             ('Algoritmos',), ''),
            (4, 'Editor e ambiente', 'Escolha um editor/IDE e configure o básico.',
             ('Editor de Texto', 'IDE'), ''),
            (5, 'Python como primeira linguagem', 'Sintaxe amigável e enorme ecossistema.',
             ('Python',), 'https://docs.python.org/pt-br/3/tutorial/'),
            (6, 'SQL e dados', 'Entenda bancos relacionais e consultas básicas.',
             ('SQL',), ''),
            (7, 'Gestão e Kanban', 'Organize estudos e projetos com fluxo visual.',
             ('Kanban', 'Gestão de Projetos'), ''),
            (8, 'Backend e APIs (visão)', 'O que acontece do lado do servidor.',
             ('Back End',), ''),
        ]

        front_steps = [
            (1, 'O que é Frontend', 'Interface, UX e o papel do frontend.',
             ('Front End',), ''),
            (2, 'HTML5', 'Estrutura semântica das páginas.',
             ('HTML5',), 'https://developer.mozilla.org/pt-BR/docs/Learn/HTML'),
            (3, 'CSS3', 'Estilo, layout e responsividade.',
             ('CSS3',), 'https://developer.mozilla.org/pt-BR/docs/Learn/CSS'),
            (4, 'JavaScript', 'Interatividade e lógica no navegador.',
             ('Javascript', 'JavaScript'), 'https://developer.mozilla.org/pt-BR/docs/Learn/JavaScript'),
            (5, 'Bibliotecas e ecossistema', 'Quando usar libs e frameworks.',
             ('Bibliotecas para Linguagem de Programação',), ''),
            (6, 'Protótipo e brainstorm', 'Ideação antes de codar a interface.',
             ('Protótipo', 'Brainstorming'), ''),
            (7, 'Diagramas de uso/classe', 'Modelar fluxos e estruturas.',
             ('Diagrama',), ''),
            (8, 'Caminho Full-Stack', 'Como o frontend se conecta ao backend.',
             ('Full-Stack',), ''),
            (9, 'Próximos passos', 'Portfólio, GitHub e projetos reais.',
             ('Front End',), 'https://roadmap.sh/frontend'),
        ]

        self._replace_etapas(fundamentos, fund_steps)
        self._replace_etapas(frontend, front_steps)
        self.stdout.write(f'Trilhas: {fundamentos.nome}, {frontend.nome}')

    def _replace_etapas(self, trilha, steps):
        trilha.etapas.all().delete()
        for ordem, titulo, descricao, topico_names, link in steps:
            topico = self._get_topico(*topico_names)
            EtapaTrilha.objects.create(
                trilha=trilha,
                ordem=ordem,
                titulo=titulo,
                descricao=descricao,
                topico=topico,
                link_externo=link or '',
            )
