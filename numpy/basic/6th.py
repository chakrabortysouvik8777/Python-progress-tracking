import numpy as np
np.random.seed(1)
data = np.random.rand(2,2)  # 100 samples, 3 features
print("Data = \n",data)
mean = np.mean(data, axis=0)
standardized_data = data - mean
print("mean = \n",mean)
print("Standardized data = ",standardized_data)
cov_matrix = np.cov(standardized_data, rowvar=False)
print("Co-varient = ",cov_matrix)
'''eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
sorted_indices = np.argsort(eigenvalues)[::-1]
sorted_eigenvalues = eigenvalues[sorted_indices]
sorted_eigenvectors = eigenvectors[:, sorted_indices]
k = 2  # Reduce to 2 dimensions
principal_components = sorted_eigenvectors[:, :k]
reduced_data = np.dot(standardized_data, principal_components)
print("Original Data Shape:", data.shape)
print("Reduced Data Shape:", reduced_data.shape)
print("Principal Components:\n", principal_components)
print("Reduced Data:\n", reduced_data[:5])  # Display first 5 samples of reduced data
'''