import './Video.css';
import React from 'react';

class VideoComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            showSnapshot: true,
            snapshotUrl: 'http://localhost:80/api/video/'+this.props.devInfo.port+'/snapshot',
            streamUrl: 'http://localhost:80/api/video/'+this.props.devInfo.port+'/stream',

        }
        this.handleVideoToggle = this.handleVideoToggle.bind(this);
    }

    handleVideoToggle() {
        const currentState = this.state.showSnapshot;
        this.setState(
            {
                showSnapshot: !currentState,
                snapshotUrl: 'http://localhost:80/api/video/'+this.props.devInfo.port+'/snapshot?ts=' + Date.now(),
            }
        );
    }

    render() {
        return (
            <div className='video'>
                <img
                    onClick={this.handleVideoToggle}
                    src={this.state.showSnapshot ? this.state.snapshotUrl : this.state.streamUrl}
                />
            </div>
        );
    }
}

export { VideoComponent }