const axios = require('axios');

test('use wrong password', () => {
    return axios.post('http://www.lcptop.com/relations/api/signin', {
        username: 'admin',
        password: '333333'
    }).then(data => {
        //fail the case
        expect(1).toBe(2);
    }).catch(err => {
        //console.log(err);
        expect(err.response.status).toBe(401);
    });
});


test('use correct password', () => {
    return axios.post('http://www.lcptop.com/relations/api/signin', {
        username: 'admin',
        password: '123456'
    }).then(response => {
        expect(response.status).toBe(200);
        expect(response.data.access_token.length).toBeGreaterThan(0);
    });
});
