import { BACKEND_URL } from '../config'
import React from 'react';

class ControlComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null
        }
        this.stopVideoService = this.stopVideoService.bind(this);
        this.startVideoService = this.startVideoService.bind(this);
    }

    stopVideoService() {
        fetch(BACKEND_URL + '/api/video/stop', {
            method: 'POST'
        })
        .then(
            (result) => {},
            (error) => {
                this.setState({
                    error: 'failed to stop video services'
                })
            }
        )
    }

    startVideoService() {
        fetch(BACKEND_URL + '/api/video/start', {
            method: 'POST'
        })
        .then(
            (result) => {},
            (error) => {
                this.setState({
                    error: 'failed to start video services'
                })
            }
        )
    }

    render() {
        return (
            <div className='control'>
                <button type="button" class="btn btn-primary btn-lg" onClick={this.startVideoService}>Start Video Service</button>
                <button type="button" class="btn btn-danger btn-lg" onClick={this.stopVideoService}>Stop Video Service</button>
                <div className='control-error text-danger'>{this.state.error}</div>
            </div>
        );
    }
}

export { ControlComponent }