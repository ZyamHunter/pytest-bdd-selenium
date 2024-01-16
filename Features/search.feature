Feature: Pesquisa

  Scenario: Pesquisar informação na página home
    Given Que esteja na página home
    When Confirmar a informação no campo de pesquisa
    Then As informações relacionadas serão exibidas
