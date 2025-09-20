import React, {useState} from "react";
import Entry from './Entry';

function SearchForm() {
    const [entries, setEntries] = useState<Entry[]>([]);

    const [loading, setLoading] = useState(false);

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        setLoading(true);
        try{
            const data = new FormData(event.currentTarget);
            const textbox = data.get('textbox') as string;
            const k = data.get('kbox') as string;
            const type = data.get('type') as string;
            const results = await SearchK(textbox, k, type);
            console.log(results);
            setEntries(results);
            //console.log(entries);
        } catch (err) {
            console.error('Failed to fetch data', err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="text" id="textbox" name="textbox"/>
                <input type="number" id="kbox" name="kbox" min="1"/>
                <select id="type" name="type">
                    <option value="cosine">Cosine Similarity</option>
                    <option value="euclid">Euclidean Distance</option>
                    <option value="dot">Dot Product</option>
                </select>
                <button type="submit">Search</button>
            </form>
            {/* <ul>
            {entries.map((entry, index) => (
                <li key={index}>Text: {entry.text}<br/>Score: {entry.score}</li>
            ))}
            </ul> */}
            {loading && <p>Loading...</p>}
            {entries && (
                <div>
                    {entries.map((entry, index) => (
                        <Entry key={index} text={entry.text} score={entry.score} />
                    ))}
                </div>
            )}
        </div>
    );
}

async function SearchK(text: string, k: string, type: string): Promise<Entry[]> {
    const response = await fetch(`http://localhost:8000/search/${text}/${k}/${type}`);
    const data = await response.json();
    const kList = Object.values(data)[0];
    return kList as Entry[];
}

export default SearchForm;