const API_BASE_URL = import .meta.env.VITE_API_BASE_URL;
if (!API_BASE_URL) {
    throw new Error('VITE_API_BASE_URL is not defined');
}
export const fetchShoes = async () => {
    const response = await fetch(`${API_BASE_URL}/shoes`);
    if (!response.ok) {
        throw new Error('Failed to fetch shoes');
    }
    return response.json();
};
    
// Uses the route /api/shoes/id
export const fetchShoeById = async (id) => {
    const resp = await fetch(`${API_BASE_URL}/shoes/${id}`);
    if (!resp.ok) {
        throw new Error('Failed to fetch shoe details');
    }
    return resp.json();
};

