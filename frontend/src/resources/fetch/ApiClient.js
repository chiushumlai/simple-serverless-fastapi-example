import axios from 'axios';
// import { aws4Interceptor } from "aws4-axios";

// const interceptor = aws4Interceptor({
//     options: {
//       region: "us-east-1",
//       service: "execute-api",
//     },
// });

// axios.interceptors.request.use(interceptor);

// No authorisation fetch request - JS Object
export const axiosClient = axios.create({
    baseURL: `https://g2653u2boa.execute-api.us-east-1.amazonaws.com/dev`,
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }
  });