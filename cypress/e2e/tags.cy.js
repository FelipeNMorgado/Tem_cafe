Cypress.Commands.add('deleteAllUsers', () => {
    cy.exec('python delete.py', { failOnNonZeroExit: true })
});

describe('teste tags', () => {
    it('cenario1', () => {
        cy.visit('/');
        cy.exec('python manage.py migrate')
        cy.deleteAllUsers();

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
        cy.get('#imgDropdown').click()
        cy.get('[data-bs-toggle="modal"]').click()
        cy.get('#inputState').select('Business')
        cy.get('#saveTagButton').click()
    })
    it('cenario2', () => {
        cy.visit('/');
        cy.exec('python manage.py migrate')
        cy.deleteAllUsers();

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
        cy.get('#imgDropdown').click()
        cy.get('[data-bs-toggle="modal"]').click()
        cy.get('#inputState').select('Trabalho')
        cy.get('#saveTagButton').click()
        cy.get('.tag-item > .btn').click()
    })
})