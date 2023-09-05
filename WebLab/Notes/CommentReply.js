import React, { useState } from 'React'

const CommentReply = (props)=>{
    //CommentReply component is a function that takes in props as an input
    //Return type JSX, which is pretty much like HTML

    //Set initial state
    //Declares isLiked to false, and specifies "setIsLiked" 
    //as the fucntion to update the state.
    const [ isLiked, setIsLiked ] = useState(false);

    return(
        <div className = "comment-text">
            <h5>{props.name}</h5>
            <p>{props.content}</p>

        </div>
    )
        //() allows us to write JSX(HTML) code inside JVS
        //{} allows us to return to JVS inside the HTML environment
        //to use variables defined inside this React Component
}

export default CommentReply