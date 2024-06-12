Cypress.Commands.add('deleteAllUsers', () => {
    cy.exec('python delete.py', { failOnNonZeroExit: true })
});

describe('teste editarperfil', () => {
    it('cenario1', () => {
        cy.visit('/');
        cy.exec('python manage.py migrate')
        cy.deleteAllUsers();

        cy.get(':nth-child(8)').click()
        cy.get('#inputFullName').type('Café Total')
        cy.get('#age4').type('25')
        cy.get('#inputgender4').select('Masculino')
        cy.get('.col-md-12 > .btn').click()
        cy.get('#inputEmail4').type('Ct@gmail.com')
        cy.get('#inputPassword4').type('12345')
        cy.get(':nth-child(4) > #inputPassword4').type('12345')
        cy.get('#gridCheck').click()
        cy.get('[type="submit"]').click()
        cy.get('#inputEmail4').type('Ct@gmail.com')
        cy.get('#inputPassword4').type('12345')
        cy.get('#inputStoreName').type('Café Total')
        cy.get('#inputAddress').type('Rua Conselheiro Theodoro')
        cy.get('#inputAddress2').type('105')
        cy.get('#inputNeighborhood').type('Zumbi')
        cy.get('#inputZip').type('50711030')
        cy.get('#gridCheck').click()
        cy.get('.btn').click()
        cy.get('#inputEmail4').type('Café Total')
        cy.get('#inputPassword4').type('12345')
        cy.get('[type="submit"]').click()
        cy.get('[href="/edit_perfil/Caf%C3%A9%20Total/"] > .btn').click()
        cy.get('#id_arq').type('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMcGkLEwpp2ukGSTKPyVC9QoHUAhBLpiVp8Q&s')
        cy.get('#id_descricao').type('Horário de funcionamento: Todos os dias 24hrs')
        cy.get('.btn').click()
    })
})