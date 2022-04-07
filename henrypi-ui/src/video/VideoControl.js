import { BACKEND_URL } from '../config'
import React from 'react';
import { VideoComponent } from './Video';
import { ControlComponent } from './Control';

class VideoControlComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            devices: [],
            isLoaded: false,
            error: null,
        }
        this.refreshVideoDevices = this.refreshVideoDevices.bind(this);
    }

    refreshVideoDevices() {
        fetch(BACKEND_URL + '/api/video')
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        devices: result,
                    })
                },
                (error) => {
                    this.setState({
                        isLoaded: false,
                        error: error,
                    })
                }
            );
    }

    componentDidMount() {
        this.refreshVideoDevices()
    }

    render() {
        const { error, isLoaded, devices } = this.state;

        if (error) {
            return <div className="text-danger">Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div className="text-info">Loading video devices...</div>;
        } else {
            return (
                <div className="videoControl">
                    {/* <ControlComponent /> */}
                    {devices.map(dev => (<VideoComponent devInfo={dev} />))}
                </div>
            );
        }
    }
}

export { VideoControlComponent }