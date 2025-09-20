interface Entry {
  text: string;
  score: number;
}

const Entry = (props: Entry) => {
    return (
        <div>
            <p>
            Text: {props.text}<br/>
            Score: {props.score}
            </p>
        </div>
    )
}
export default Entry