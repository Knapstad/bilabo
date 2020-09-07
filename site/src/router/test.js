const sanityClient = require('@sanity/client');
const client = sanityClient({
  projectId: 'bwpvihdh',
  dataset: 'production',
  useCdn: false,
});

let query = "*[_type=='post']['slug']['current']";
let loading = true;
const stuff = client
  .fetch(query, {})
  .then(function (data) {
    return data;
  })
  .then((loading = false));

let data = stuff;
while (loading) {
  continue;
}

export default data;
