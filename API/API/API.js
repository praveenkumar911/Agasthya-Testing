const mongoose = require('mongoose')

const APISchema = new mongoose.Schema({
    Name : {
        type : String,
        required : true
    },
    SC1 : {
        type : Number,
        required : true
    },
    SC2 : {
        type : Number,
        required : true
    },
    SC3 : {
        type : Number,
        required : true
    },
    Gender : {
        type : String,
        required : true
    }

})

const API = mongoose.model('API',APISchema)

module.exports = API