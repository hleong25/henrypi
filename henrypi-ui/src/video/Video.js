import { BACKEND_URL } from '../config'
import './Video.css';
import React from 'react';

class VideoComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            showSnapshot: true,
            snapshotUrl: BACKEND_URL + '/api/video/' + this.props.devInfo.port + '/snapshot',
            streamUrl: BACKEND_URL + '/api/video/' + this.props.devInfo.port + '/stream',

        }
        this.handleVideoToggle = this.handleVideoToggle.bind(this);
    }

    handleVideoToggle() {
        const currentState = this.state.showSnapshot;
        this.setState(
            {
                showSnapshot: !currentState,
                snapshotUrl: BACKEND_URL + '/api/video/' + this.props.devInfo.port + '/snapshot?ts=' + Date.now(),
            }
        );
    }

    render() {
        return (
            <div className='video'>
                <img
                    src={this.state.showSnapshot ? this.state.snapshotUrl : this.state.streamUrl}
                    onClick={this.handleVideoToggle}
                    alt={this.props.devInfo.device}
                    title={this.props.devInfo.device}
                />
            </div>
        );
    }
}

export { VideoComponent }