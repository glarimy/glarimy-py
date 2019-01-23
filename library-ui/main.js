import React from "react";
import ReactDOM from 'react-dom';

class Library extends React.Component{
	constructor(props){
		super(props);
        this.state = {
            found: false,
            error: null,
            isbn: null,
            book: {}
        }
        this.onIsbn = (e) => {this.setState({isbn: e.target.value, found: false, error: null})}
        this.onFind = () => {
            this.setState({found: false});
            fetch('http://localhost:5000/library/book/'+this.state.isbn)
            .then(response =>{
                if(response.ok)
                    return response.json();
                throw response.status;
            }).then(book =>{this.setState({book: book, found: true});
            }).catch(error => {this.setState({error: error==404? 'Book not found':'Internal Error'})})
        }
    }

	render(){
        return (
            <div>
                <h1>Cloud Library</h1>
                <hr/>
                Find Book <input placeholder='ISBN' onChange={this.onIsbn} defaultValue={this.state.isbn}/>
                <button onClick={this.onFind}>Find</button>
                <hr/>
                <div>{this.state.error}</div>
                <div style={{display: this.state.found?'block':'none'}}>
                <table>
                    <tr><td>ISBN</td><td>{this.state.book.isbn}</td></tr>
                    <tr><td>Title</td><td>{this.state.book.title}</td></tr>
                    <tr><td>Price</td><td>{this.state.book.price}</td></tr>
                </table>
                </div>
            </div>
        );
	}
};


ReactDOM.render(<Library />, document.getElementById('library'));