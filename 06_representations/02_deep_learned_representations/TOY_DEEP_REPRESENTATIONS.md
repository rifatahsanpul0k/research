# Toy deep representations

Synthetic values only; no project data are read.

*Linear layer:* x=(2,1)^T, W=[[1,0],[0,2]], b=(1,-1)^T gives ReLU(Wx+b)=(3,1)^T.

*Autoencoder:* W_e=[1,1] gives z=3; W_d=(0.5,0.25)^T gives xhat=(1.5,0.75)^T and squared error 0.3125.

*VAE:* μ=(0.4,-0.2), logσ²=(-1.386,0), so σ=(0.5,1); ε=(1,-1) gives z=(0.9,-1.2).

*Contrastive:* z=(1,0), z+=(0.8,0.6), z-=(0,1) have cosine similarities 0.8 and 0. A declared pair is an assumption.

*GCN:* A~= [[1,1],[1,1]], D~=diag(2,2), H=(2,0)^T and W=1 give normalized propagation (1,1)^T.

*Attention:* q=(1,0), k1=(1,0), k2=(0,1), d=2 gives logits (0.707,0), softmax≈(0.67,0.33); values (2,0),(0,2) give (1.34,0.66).

*Graph attention:* scores (1,0) give α=(0.731,0.269), a weighting rather than causal importance.

*Shared/private:* z_R=(1,2), z_A=(1,1), one possible convention is z_shared=(1,1), residuals (0,1) and (0,0); decomposition is not identifiable biology.
