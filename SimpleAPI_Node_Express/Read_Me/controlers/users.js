import { v4 as uuidv4 } from 'uuid';

let users = [
    // {
    //     "FirstName": "John",
    //     "LastName": "Tall",
    //     "Age": "20"
    // },
    // {
    //     "FirstName": "Jane",
    //     "LastName": "Big",
    //     "Age": "21"
    // }
]

export const createUser = (req, res ) => {
    const user = req.body;

    users.push({ ...user, id:uuidv4() }); // spread (spread opera tor) the property of current user and added id

}

export  const getusers = (req, res) => {
    res.send(users);
}

export const getuserId = (req, res) =>{
    const { id } = req.params;
    const foundUser = users.find((user) => user.id === id);
    res.send(req.params);
} 

export const deleteUser =  (req, res) =>{
    const { id } = req.params;

    users = users.filter((user) => user.id != id); // filter removes the elemen for those the function returns false
}

export const updateUser =  (req, res) =>{
    const { id } = req.params;
    const { firstName, lastName, age } = req.body;

    const UserToBeUpdated = users.find((user) => user.id === id);

    if(firstName) UserToBeUpdated.firstName = firstName;
    
    if(lastName) UserToBeUpdated.lastName = lastName;

    if(age) UserToBeUpdated.age = age;

    res.send(`User with the ${id} has been updated`);
}