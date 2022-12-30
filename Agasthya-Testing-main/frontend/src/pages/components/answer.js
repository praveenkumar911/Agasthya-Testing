import  {useEffect,useState} from 'react';
import * as React from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionDetails from '@mui/material/AccordionDetails';
import AccordionSummary from '@mui/material/AccordionSummary';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import "../components/Questions.css"
const Answers=()=>{
    const[data,setData]=useState([])
    const [expanded, setExpanded] = React.useState(false);

    const handleChange = (panel) => (event, isExpanded) => {
    setExpanded(isExpanded ? panel : false);
  };

    useEffect(()=>{
        
        fetch('/questions?answered=true').then(response=>response.json()).then(json=>{
           setData(json.items)
           console.log(json)
            
        }).catch(e=>{
            console.log(e)
        })
    },[setData])
    return(
        <>
       {data.map(val=>{
            return(
                <>
                {val.answers.map(val1=>{
                      if (val1.correct=== true) {
                    return(
                        <div className='Answers'>
                        <>
                        <Accordion expanded={expanded === 'panel1'} onChange={handleChange('panel1')}>
                        <AccordionSummary
                        expandIcon={<ExpandMoreIcon />}
                        aria-controls="panel1bh-content"
                        id="panel1bh-header"
                        > 
                        <Typography sx={{ width: '80%', flexShrink: 0 }}>
                            Q.{val.asr}
                        </Typography>
                        </AccordionSummary>
                        <AccordionDetails>
                        <Typography> 
                        A. {val1.telugu_text}
                        </Typography>
                        </AccordionDetails>
                        </Accordion> 
                      </></div>
                    )}
                })}
                </> 
            )
        })}
        
        </>
    )

}


export default Answers;





