const express = require('express')
const cors = require('cors')
const app = express()
const mongoose = require('mongoose')
app.use(express.json())
app.use(cors())
const PORT = 4000
app.listen(PORT, () => {
    console.log(`Server is running on PORT ${PORT}...`)
})

// connect database
mongoose.connect("mongodb://0.0.0.0:27017/API", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}).then(() => {
    console.log('Database connected..')
})

// create post route
const API = require('./API')

app.post('/add-API', async(req,res) => {
    const Api = new API(req.body)
    try{
        await Api.save()
        res.status(201).json({
            status: 'Success',
            data : {
                Api
            }
        })
    }catch(err){
        res.status(500).json({
            status: 'Failed',
            message : err
        })
    }
}) 

// create get route
app.get('/get-Api', async (req,res) => {
    const Apis = await API.find({})
    try{
        res.status(200).json({
            status : 'Success',
            data : {
                Apis
            }
        })
    }catch(err){
        res.status(500).json({
            status: 'Failed',
            message : err
        })
    }
})