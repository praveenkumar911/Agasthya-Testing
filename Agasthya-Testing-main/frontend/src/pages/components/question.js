import  {useEffect,useState} from 'react';
import "../components/Questions.css"
import ReactAudioPlayer from 'react-audio-player';
import * as React from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import CloseIcon from '@mui/icons-material/Close';
import Slide from '@mui/material/Slide';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import ImportContactsIcon from '@mui/icons-material/ImportContacts';
import DeleteOutlineIcon from '@mui/icons-material/DeleteOutline';
import PauseCircleOutlineIcon from '@mui/icons-material/PauseCircleOutline';
import PlayCircleIcon from '@mui/icons-material/PlayCircle';

const Transition = React.forwardRef(function Transition(props, ref) {
  return <Slide direction="up" ref={ref} {...props} />;
});
function Questions(){
    const[data,setData]=useState([])
    const[mobile,setMobile]=useState()
    const[grade,setGrade]=useState()
    const[asr,setAsr]=useState()
    const[subject,setSubject]=useState()
    const[id,setId]=useState()
    const[translation,setTranslation]=useState()
    const [open, setOpen] = React.useState(false);
    const[id1,setId1]=useState()

    const handleClickOpen = () => {
      setOpen(true);
    };
  
    const handleClose = () => {

      setOpen(false);
    };
  
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
    const handleId=(id1)=>{
        setId1(id1)
        console.log(id1)
        GetAnswers(id1);
   }
    const GetAnswers=(id1)=>{
        const data={
            "id":id1
        }
        fetch(`/questions/${data.id}/answers/correct`,{
            method:'GET',
            /*headers:{
                'Content-Type':'application/json',
                'Access-Control-Allow-Origin':'*',
            },
            body:JSON.stringify(data)*/
        }).then(response=>{
            console.log(response)
          
        }).catch(e=>{
            console.log(e)
        })
    }
    const Delete=(id)=>{
      const data={
        "id":id
      }
    fetch(`/questions/${data.id}`,{
      method:'DELETE',
      headers:{
        'Content-Type':'application/json',
        "Access-Control-Allow-Origin":"*",
      }
    }).then(response=>{
      console.log(response)
       window.location.reload();
    }).catch(e=>{
      console.log(e)
    })
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
            />       
            <Button variant="outlined" startIcon={<DeleteOutlineIcon/>}  onClick={(e)=>{Delete(val.id)}}></Button>
<div className='Standard'> Standard{val.grade},{val.subject}</div>
<div className="A2">
                <input className="text"   onChange={(e)=>Handleasr(e,val.id,val.grade,val.subject,val.from_mobile)} defaultValue={val.asr}/>
                </div><br></br>
<div className='book'>
                <Button  variant="outlined" onClick={() => {handleId(val.id);handleClickOpen();}}>
            <ImportContactsIcon />
          </Button> </div>
                <div  className="A3" >
                    <input className="text1" onChange={(e)=>Handletranslation(e,val.id,val.grade,val.subject,val.from_mobile)} defaultValue={val.translation} />
                    </div> <br/><br/>
                    <button onClick={Edit} >submit</button>
                </div> 
        
                
            )
        })}
         <Dialog
        fullScreen
        open={open}
        onClose={handleClose}
        TransitionComponent={Transition}
      >
        <AppBar sx={{ position: 'relative' }}>
          <Toolbar>
            <IconButton
              edge="start"
              color="inherit"
              onClick={handleClose}
              aria-label="close"
            >
              <CloseIcon />
            </IconButton>
            <Typography sx={{ ml: 2, flex: 1 }} variant="h6" component="div">
              Answers for asr
            </Typography>
            <Button autoFocus color="inherit" onClick={handleClose}>
              save
            </Button>
          </Toolbar>
        </AppBar>
        <FormControl>
        <Box
      sx={{
        width: 500,
        maxWidth: '100%',
      }}
    >
      <TextField  fullWidth label="fullWidth" id="fullWidth" />
    </Box>
      <RadioGroup
        aria-labelledby="demo-radio-buttons-group-label"
        defaultValue="Answer1"
        name="radio-buttons-group"
      >
        <FormControlLabel value="Answer1" control={<Radio />} label="Answer1" />
      </RadioGroup>
    </FormControl>
      </Dialog>
        </>
    )

}

export default Questions;