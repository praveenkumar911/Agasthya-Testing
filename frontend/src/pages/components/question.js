import  {useEffect,useState} from 'react';
import "../components/Questions.css"
import ReactAudioPlayer from 'react-audio-player';
import Questions1 from '../questions';

function Questions(){
    const[data,setData]=useState([])
    const[mobile,setMobile]=useState()
    const[grade,setGrade]=useState()
    const[asr,setAsr]=useState()
    const[subject,setSubject]=useState()
    const[id,setId]=useState()
    const[translation,setTranslation]=useState()
  
    useEffect(()=>{
        
        fetch('/questions').then(response=>response.json()).then(json=>{
            setData(json.items)
        }).catch(e=>{
            console.log(e)
        })
    },[setData])
    const Handleasr=(e,id,grade,subject,from_mobile)=>{
       
        setAsr(e.target.value)
        setId(id)
        setGrade(grade)
        setSubject(subject)
        setMobile(from_mobile)
        console.log(asr,id)
    }
    const Handletranslation=(e,id,grade,subject,from_mobile)=>{
      
        setTranslation(e.target.value)
        setId(id)
        setGrade(grade)
        setSubject(subject)
        setMobile(from_mobile)
        console.log(translation)
    }
    const Edit=async () =>{
        const data={
            "id":id,      
            "from_mobile": mobile,
            "grade": grade,
            "subject": subject,
            "asr":  asr,
            "translation": translation,
        }
        fetch(`/questions/${data.id}`,{
            method:'PATCH',
            headers:{
                'Content-Type':'application/json',
                'Access-Control-Allow-Origin':'*',
            },
            body:JSON.stringify(data)
        }).then(response=>{
            console.log(response)
            window.location.reload();
        }).catch(e=>{
            console.log(e)
        })
    }
    return(
        <>
        {data.map(val=>{
            return(
            
                <div className="A1"><br/>
                        <ReactAudioPlayer
            src={val.audio_url}
            autoPlay
            controls
            className='audio'
            />        <div class><Questions1/> </div>      
<div className="A3">
                <input className="text"   onChange={(e)=>Handleasr(e,val.id,val.grade,val.subject,val.from_mobile)} defaultValue={val.asr}/>
                </div>
                <div  className="A4">
                    <input className="text1" onChange={(e)=>Handletranslation(e,val.id,val.grade,val.subject,val.from_mobile)} defaultValue={val.translation} />
                    </div> <br/><br/>
                    <button onClick={Edit}>submit</button>
                </div>
                
            )
        })}
        
        </>
    )

}

export default Questions;