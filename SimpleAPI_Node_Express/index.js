import express from 'express';
import bodyParser from 'body-parser';

import usersRoutes from './routes/users.js'; // The import is default it can be named anything
 
const app = express();
const PORT = 5000;

app.use(bodyParser.json()); // Means we are using JSON

app.use('/users', usersRoutes);

app.get('/', (req, res) =>{res.send('Hello home page')
});


app.listen(PORT, () => console.log(`server running on port: http://localhost:${PORT}`));
