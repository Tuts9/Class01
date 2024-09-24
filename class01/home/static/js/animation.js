// Animações para o hero section
const textHome = document.querySelector('#text-home');
const imgHome = document.querySelector('#img-home');

function startAnimationHome(elem) {
  gsap.fromTo(elem,
    {
      opacity: 0,
      x: -250,
      ease: "power1.out",
    },
    {
      opacity: 1,
      x: 0,
      duration: 2,
    }
  );
}
startAnimationHome(textHome);
startAnimationHome(imgHome);
// Fim das animações do hero section

// ---------------------------------------------------------------------

// Animações na página de cada tópico
const titleTool = document.querySelector('#title-tool');
const imgTopic = document.querySelector('#img-topic');

// Animação do título
function startAnimationTextTopic(elem) {
  gsap.fromTo(elem, {
    opacity: 0,
    y: -150,
    ease: "power1.out"
  }, {
    opacity: 1,
    y: 0,
    duration: 2
  });
}
startAnimationTextTopic(titleTool);

// Animação da imagem
function startAnimationImg(elem) {
  gsap.fromTo(elem, {
    x: -500,
    opacity: 0,
    ease: 'power1.out'
  }, {
    x: 0,
    opacity: 1,
    duration: 1.7
  })
}
startAnimationImg(imgTopic);

// Animação de entrada dos cards de ferramentas de cada tópico
const cardTools = document.querySelectorAll('#card-tool');

cardTools.forEach(cardTool => {
  gsap.fromTo(cardTool, {
    x: -600,
    opacity: 0,
    ease: 'power1.out'
  }, {
    x: 0,
    opacity: 1,
    duration: 2,
    scrollTrigger: {
      trigger: cardTool,
      start: 'top 80%',
      end: 'bottom 95%',
      scrub: true
    }
  });
});

// Fim das animações da página de cada tópico

// ------------------------------------------------------------------------------------------------

// Animação dos cards da página de todos os tópicos -- EM BREVE SERÃO ALTERADOS
const cards = document.querySelectorAll('.card')

if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
  // GSAP e ScrollTrigger estão disponíveis
  ScrollTrigger.batch(cards, {
      onEnter: batch => gsap.to(batch, {
          autoAlpha: 1, // Opacidade e visibilidade
          stagger: 0.1  // Animação escalonada
      }),
  });
} else {
  // GSAP ou ScrollTrigger não estão disponíveis
  cards.forEach(card => {
      card.classList.remove = 'opacity-0';
      card.classList.add = 'opacity-1';
  });
}
