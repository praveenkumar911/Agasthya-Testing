import { useState } from "react"
import * as React from 'react';
import Stack from '@mui/material/Stack';
import TextField from '@mui/material/TextField';
import Axios from 'axios';
const Dashboard=()=>{
   const [name,setName]=useState()
   const[score1,setScore1]=useState()
   const[score2,setScore2]=useState()
   const[score3,setScore3]=useState()
   const[gender,setGender]=useState()
   const[data,setData]=useState()
   const handleName=(e)=>{
     setName(e.target.value)
   }
   const handlescore1=(e)=>{
    setScore1(e.target.value)
  }
  const handlescore2=(e)=>{
    setScore2(e.target.value)
  }
 const  handlescore3=(e)=>{
    setScore3(e.target.value)
  }
 const  handleGender=(e)=>{
    setGender(e.target.value)
  }
   const handlepost=()=>{
    const body={
        Name:name,
        SC1:score1,
        SC2:score2,
        SC3:score3,
        Gender:gender
    }
    Axios.post("http://localhost:4000/add-API",body)
   }

   React.useEffect(()=>{
    fetch("http://localhost:4000/get-API").then(response=>response.json()).then(json=>{
      setData(json.Apis)
    }).catch(e=>{
      console.log(e)
    })
   },[setData])

   /*
   <label>Name</label>
    <input type='text' onChange={handleName}/>
    <label>SC1</label>
    <input type='text'onChange={handlescore1}/>
    <label>sc2</label>
    <input type='text'onChange={handlescore2}/>
    <label>sc3</label>
    <input type='text' onChange={handlescore3} />
    <label>gender</label>
    <input type='text'onChange={handleGender}/>
    <button onClick={handlepost}>submit</button>*/
   return(
    <>
    {data.map(val=>{
      return(
        <>{val.Name}</>
      )
    })}
    </>
   )
}
export default Dashboard;