import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            ledstatus: [],
            servoposition: [],
            motordirection: []
        };
    }

    loadStatus = () => {
        fetch("http://localhost:5000/api/ledstatus")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        ledstatus: result.ledstatus,
                    });
                },
                (error) => {
                    this.setState({
                        error,
                    });
                }
            )
    }

    loadPosition = () => {
        fetch("http://localhost:5001/api/servoposition")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        servoposition: result.servoposition,
                    });
                },
                (error) => {
                    this.setState({
                        error,
                    });
                }
            )
    }
    loadDirection = () => {
        fetch("http://localhost:5002/api/motordirection")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        motordirection: result.motordirection,
                    });
                },
                (error) => {
                    this.setState({
                        error,
                    });
                }
            )
    }



    componentDidMount() {
        this.loadStatus();
        this.loadPosition();
        this.loadDirection();
    }

    render() {
        const {error, ledstatus, servoposition, motordirection} = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else {
            return (
                <div>
                    <h1>Raspberry Pi Monolith App</h1>
                    <h2>LED Status</h2>
                    <ul>
                    <button onMouseDown={(e) => {
						e.preventDefault();
						window.location.href='http://localhost:5000/api/ledon';
						}}
						onMouseUp={(e) => {
							e.preventDefault();
							window.location.href='http://localhost:5000/api/ledoff';
							}}>LED On</button>
                    
                    </ul>
                    <h2>Servo Position </h2>
                    <ul>
                    <button onMouseDown={(e) => {
						e.preventDefault();
						window.location.href='http://localhost:5001/api/min';
						}}>Min</button>
                    <button onMouseDown={(e) => {
						e.preventDefault();
						window.location.href='http://localhost:5001/api/mid';
						}}>Mid</button>
                    <button onMouseDown={(e) => {
						e.preventDefault();
						window.location.href='http://localhost:5001/api/max';
						}}>Max</button>
                    </ul>
                    <h2>Motor Direction </h2>
                    <ul>
                    <button onMouseDown={(e) => {
						e.preventDefault();
						window.location.href='http://localhost:5002/api/up';
						}}
						onMouseUp={(e) => {
							e.preventDefault();
							window.location.href='http://localhost:5002/api/stop';
							}}> Forward </button>
                    <button onMouseDown={(e) => {
						e.preventDefault();
						window.location.href='http://localhost:5002/api/down';
						}}
						onMouseUp={(e) => {
							e.preventDefault();
							window.location.href='http://localhost:5002/api/stop';
							}}> Backward </button>
                    <button onMouseDown={(e) => {
						e.preventDefault();
						window.location.href='http://localhost:5002/api/left';
						}}
						onMouseUp={(e) => {
							e.preventDefault();
							window.location.href='http://localhost:5002/api/stop';
							}}> Left </button>
                    <button onMouseDown={(e) => {
						e.preventDefault();
						window.location.href='http://localhost:5002/api/right';
						}}
						onMouseUp={(e) => {
							e.preventDefault();
							window.location.href='http://localhost:5002/api/stop';
							}}> Right </button>
                    
                    </ul>

                </div>
            );
        }
    }
}

ReactDOM.render(
    <App/>,
    document.getElementById('root')
);
