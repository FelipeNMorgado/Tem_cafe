Cypress.Commands.add('deleteAllUsers', () => {
    cy.exec('python delete.py', { failOnNonZeroExit: true })
});

describe('teste favoritarcafeteria', () => {
    it('cenario1', () => {
        cy.visit('/');
        cy.exec('python manage.py migrate')
        cy.deleteAllUsers();

        cy.get(':nth-child(8)').click()
        cy.get('#inputFullName').type('Café do Zé')
        cy.get('#age4').type('25')
        cy.get('#inputgender4').select('Masculino')
        cy.get('.col-md-12 > .btn').click()
        cy.get('#inputEmail4').type('ze@gmail.com')
        cy.get('#inputPassword4').type('12345')
        cy.get(':nth-child(4) > #inputPassword4').type('12345')
        cy.get('#gridCheck').click()
        cy.get('[type="submit"]').click()
        cy.get('#inputEmail4').type('ze@gmail.com')
        cy.get('#inputPassword4').type('12345')
        cy.get('#inputStoreName').type('Café do Zé')
        cy.get('#inputAddress').type('Rua Conselheiro Theodoro')
        cy.get('#inputAddress2').type('105')
        cy.get('#inputNeighborhood').type('Zumbi')
        cy.get('#inputZip').type('50711030')
        cy.get('#gridCheck').click()
        cy.get('.btn').click()
        cy.get('form > :nth-child(6)').click()
        cy.get('#inputFullName').type('Tonho')
        cy.get('#age4').type('28')
        cy.get('#inputgender4').select('Masculino')
        cy.get('.col-md-12 > .btn').click()
        cy.get('#inputEmail4').type('Tonho@gmail.com')
        cy.get('#inputPassword4').type('12345')
        cy.get(':nth-child(4) > #inputPassword4').type('12345')
        cy.get('#gridCheck').click()
        cy.get('[type="submit"]').click()
        cy.get('#inputEmail4').type('Tonho')
        cy.get('#inputPassword4').type('12345')
        cy.get('[type="submit"]').click()
        cy.get('.group-item > :nth-child(1) > a').click()
        cy.get('.card-body > .btn').click()
        cy.get('.form > .ui').click()
        cy.get('#logo').click()
    })
    it('cenario2', () => {
        cy.visit('/');
        cy.exec('python manage.py migrate')
        cy.deleteAllUsers();

        cy.get(':nth-child(8)').click()
        cy.get('#inputFullName').type('Cafeteria do Zé')
        cy.get('#age4').type('25')
        cy.get('#inputgender4').select('Masculino')
        cy.get('.col-md-12 > .btn').click()
        cy.get('#inputEmail4').type('ze@gmail.com')
        cy.get('#inputPassword4').type('12345')
        cy.get(':nth-child(4) > #inputPassword4').type('12345')
        cy.get('#gridCheck').click()
        cy.get('[type="submit"]').click()
        cy.get('#inputEmail4').type('ze@gmail.com')
        cy.get('#inputPassword4').type('12345')
        cy.get('#inputStoreName').type('Cafeteria do Zé')
        cy.get('#inputAddress').type('Rua Conselheiro Theodoro')
        cy.get('#inputAddress2').type('105')
        cy.get('#inputNeighborhood').type('Zumbi')
        cy.get('#inputZip').type('50711030')
        cy.get('#gridCheck').click()
        cy.get('.btn').click()
        cy.get('form > :nth-child(6)').click()
        cy.get('#inputFullName').type('Tonho')
        cy.get('#age4').type('28')
        cy.get('#inputgender4').select('Masculino')
        cy.get('.col-md-12 > .btn').click()
        cy.get('#inputEmail4').type('Tonho@gmail.com')
        cy.get('#inputPassword4').type('12345')
        cy.get(':nth-child(4) > #inputPassword4').type('12345')
        cy.get('#gridCheck').click()
        cy.get('[type="submit"]').click()
        cy.get('#inputEmail4').type('Tonho')
        cy.get('#inputPassword4').type('12345')
        cy.get('[type="submit"]').click()
        cy.get('.group-item > :nth-child(1) > a').click()
        cy.get('.card-body > .btn').click()
        cy.get('.form > .ui').click()
        cy.get('#logo').click()
        cy.get('.group-item > :nth-child(1) > a').click()
        cy.get('.card-body > .btn').click()
        cy.get('.form > .ui').click()
        cy.get('#logo').click()
    })
})