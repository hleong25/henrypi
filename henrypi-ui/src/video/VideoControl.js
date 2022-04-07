// import './VideoControl.css';
import React from 'react';
import { VideoComponent } from './Video';

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
        fetch('http://localhost:80/api/video')
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
            return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading...</div>;
        } else {
            return (
                <div className="videoControl">
                    {devices.map(dev => ( <VideoComponent devInfo={dev} />))}
                </div>
            );
        }
    }
}

export { VideoControlComponent }