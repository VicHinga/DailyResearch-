import express from 'express';

import { createUser, getusers, getuserId, deleteUser, updateUser } from '../controlers/users.js'; 

const router = express.Router();



//Need to get users from Server
router.get('/', getusers);

router.get('/:id', getuserId );


//Need to send from Front End to Server
router.post('/', createUser ); 

//Need to patch() to update Server without overriding
router.patch('/:id', updateUser);

//Need to delete() to erase from Server
router.delete('/:id', deleteUser);


export default router;