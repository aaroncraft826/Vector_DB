import React, {useState} from "react";

function InsertForm() {
    const [outcome, setOut] = useState("");
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        setLoading(true);
        setOut("");
        try{
            const data = new FormData(event.currentTarget);
            const textbox = data.get('textbox') as string;
            const result = await Insert(textbox);
            console.log(result);
            setOut("Insert successful!");
        } catch (err) {
            console.error('Failed to fetch data', err);
            setOut("Insert failed.");
        } finally {
            setLoading(false);
        }
    };
    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="text" id="textbox" name="textbox"/>
                <button type="submit">Insert</button>
            </form>
            {loading && <p>Loading...</p>}
            {outcome && (
                <div>
                    {outcome}
                </div>
            )}
        </div>
    );
}

async function Insert(text: string): Promise<boolean> {
    const response = await fetch(`http://localhost:8000/insert/${text}`);
    const data = await response.json();
    return data
}

export default InsertForm;