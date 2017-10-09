import React, { Component } from 'react';
import LinearProgress from 'material-ui/LinearProgress';
import FlatButton from 'material-ui/FlatButton';


class Sammenlikning extends Component {

    constructor(props) {
        super(props);

        this.state = {
            progress: {
              label: 'IKKE STARTET',
              total: 100,
              count: 0
            }
        };
    }

    startSammenlikning = (e) => {
        console.log(e);
        this.doFetch('http://localhost:5000/longtask', 'POST', {}, 'progress');
        this.setState({
            started: true
        });
    }

    doFetch(url, method, payload, stateChange) {
      var that = this;
      fetch(url, {
        method: method,
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload)
      })
      .then(function(response){
        return response.json();
      })
      .then(function(jsonResponse){
        that.setState({stateChange:jsonResponse.status});
      })
      .catch((error) => {
        console.error(error);
      });

    }


     render() {

       return (
         <div>
           <FlatButton label="Start Sammenlikning" onClick={this.startSammenlikning} />
           {this.state.progress.label} <LinearProgress mode="determinate" max={this.state.progress.total} min={this.state.progress.count} value={this.state.progress.count} />
         </div>
       )
     }

  }

  export default Sammenlikning;
